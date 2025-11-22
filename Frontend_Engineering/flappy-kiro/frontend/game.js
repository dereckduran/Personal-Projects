class FlappyKiroGame {
    constructor(canvas) {
        this.canvas = canvas;
        this.ctx = canvas.getContext('2d');
        this.reset();
        this.setupDifficulty();
    }

    reset() {
        this.ghosty = {
            x: 100,
            y: 300,
            width: 40,
            height: 40,
            velocity: 0,
            gravity: 0.5,
            jumpPower: -8
        };
        
        this.walls = [];
        this.score = 0;
        this.gameRunning = false;
        this.gameOver = false;
        this.wallSpacing = 300;
        this.lastWallX = 400;
    }

    setupDifficulty() {
        const difficulties = {
            easy: { gravity: 0.4, jumpPower: -9, wallSpeed: 2, gapSize: 180 },
            medium: { gravity: 0.5, jumpPower: -8, wallSpeed: 3, gapSize: 150 },
            hard: { gravity: 0.6, jumpPower: -7, wallSpeed: 4, gapSize: 120 }
        };
        
        this.difficulty = difficulties[this.selectedDifficulty] || difficulties.easy;
        this.ghosty.gravity = this.difficulty.gravity;
        this.ghosty.jumpPower = this.difficulty.jumpPower;
    }

    setDifficulty(level) {
        this.selectedDifficulty = level;
        this.setupDifficulty();
    }

    start() {
        const span = telemetry.startSpan('game_start', {
            difficulty: this.selectedDifficulty
        });
        
        this.reset();
        this.setupDifficulty();
        this.gameRunning = true;
        this.gameLoop();
        
        telemetry.endSpan(span);
    }

    jump() {
        if (this.gameRunning && !this.gameOver) {
            const span = telemetry.startSpan('player_jump');
            this.ghosty.velocity = this.ghosty.jumpPower;
            telemetry.endSpan(span);
        }
    }

    update() {
        if (!this.gameRunning || this.gameOver) return;

        // Update Ghosty
        this.ghosty.velocity += this.ghosty.gravity;
        this.ghosty.y += this.ghosty.velocity;

        // Generate walls
        if (this.walls.length === 0 || this.lastWallX - this.walls[this.walls.length - 1].x > this.wallSpacing) {
            this.generateWall();
        }

        // Update walls
        this.walls.forEach(wall => {
            wall.x -= this.difficulty.wallSpeed;
        });

        // Remove off-screen walls and update score
        this.walls = this.walls.filter(wall => {
            if (wall.x + wall.width < 0) {
                if (!wall.scored) {
                    this.score++;
                    wall.scored = true;
                    telemetry.addEvent(telemetry.startSpan('score_update'), 'score_increased', {
                        newScore: this.score,
                        difficulty: this.selectedDifficulty
                    });
                }
                return false;
            }
            return true;
        });

        // Check collisions
        this.checkCollisions();

        // Check boundaries
        if (this.ghosty.y < 0 || this.ghosty.y + this.ghosty.height > this.canvas.height) {
            this.endGame();
        }
    }

    generateWall() {
        const gapY = Math.random() * (this.canvas.height - this.difficulty.gapSize - 100) + 50;
        
        // Top wall
        this.walls.push({
            x: this.canvas.width,
            y: 0,
            width: 60,
            height: gapY,
            scored: false
        });
        
        // Bottom wall
        this.walls.push({
            x: this.canvas.width,
            y: gapY + this.difficulty.gapSize,
            width: 60,
            height: this.canvas.height - (gapY + this.difficulty.gapSize),
            scored: false
        });
        
        this.lastWallX = this.canvas.width;
    }

    checkCollisions() {
        const ghostyRect = {
            x: this.ghosty.x,
            y: this.ghosty.y,
            width: this.ghosty.width,
            height: this.ghosty.height
        };

        for (let wall of this.walls) {
            if (this.isColliding(ghostyRect, wall)) {
                this.endGame();
                break;
            }
        }
    }

    isColliding(rect1, rect2) {
        return rect1.x < rect2.x + rect2.width &&
               rect1.x + rect1.width > rect2.x &&
               rect1.y < rect2.y + rect2.height &&
               rect1.y + rect1.height > rect2.y;
    }

    endGame() {
        const span = telemetry.startSpan('game_end', {
            finalScore: this.score,
            difficulty: this.selectedDifficulty
        });
        
        this.gameOver = true;
        this.gameRunning = false;
        
        telemetry.endSpan(span);
        
        // Trigger game over event
        if (this.onGameOver) {
            this.onGameOver(this.score, this.selectedDifficulty);
        }
    }

    render() {
        // Clear canvas
        this.ctx.fillStyle = '#87CEEB';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        // Draw ground
        this.ctx.fillStyle = '#98FB98';
        this.ctx.fillRect(0, this.canvas.height - 50, this.canvas.width, 50);

        // Draw Ghosty
        this.ctx.fillStyle = '#FFFFFF';
        this.ctx.strokeStyle = '#000000';
        this.ctx.lineWidth = 2;
        
        // Simple ghost shape
        this.ctx.beginPath();
        this.ctx.arc(this.ghosty.x + this.ghosty.width/2, this.ghosty.y + this.ghosty.height/2, this.ghosty.width/2, 0, Math.PI * 2);
        this.ctx.fill();
        this.ctx.stroke();
        
        // Ghost eyes
        this.ctx.fillStyle = '#000000';
        this.ctx.beginPath();
        this.ctx.arc(this.ghosty.x + 12, this.ghosty.y + 15, 3, 0, Math.PI * 2);
        this.ctx.arc(this.ghosty.x + 28, this.ghosty.y + 15, 3, 0, Math.PI * 2);
        this.ctx.fill();

        // Draw walls
        this.ctx.fillStyle = '#228B22';
        this.ctx.strokeStyle = '#006400';
        this.ctx.lineWidth = 3;
        
        this.walls.forEach(wall => {
            this.ctx.fillRect(wall.x, wall.y, wall.width, wall.height);
            this.ctx.strokeRect(wall.x, wall.y, wall.width, wall.height);
        });
    }

    gameLoop() {
        this.update();
        this.render();
        
        if (this.gameRunning) {
            requestAnimationFrame(() => this.gameLoop());
        }
    }
}