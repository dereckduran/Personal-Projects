class FlappyKiroApp {
    constructor() {
        this.currentScreen = 'menu';
        this.selectedDifficulty = 'easy';
        this.game = null;
        this.initializeElements();
        this.setupEventListeners();
        this.showScreen('menuScreen');
    }

    initializeElements() {
        // Screens
        this.menuScreen = document.getElementById('menuScreen');
        this.gameScreen = document.getElementById('gameScreen');
        this.gameOverScreen = document.getElementById('gameOverScreen');
        this.leaderboardScreen = document.getElementById('leaderboardScreen');

        // Game elements
        this.canvas = document.getElementById('gameCanvas');
        this.scoreDisplay = document.getElementById('score');
        this.difficultyDisplay = document.getElementById('difficulty');

        // Menu elements
        this.difficultyButtons = document.querySelectorAll('.difficulty-btn');
        this.startGameBtn = document.getElementById('startGame');
        this.showLeaderboardBtn = document.getElementById('showLeaderboard');

        // Game over elements
        this.finalScoreDisplay = document.getElementById('finalScore');
        this.finalDifficultyDisplay = document.getElementById('finalDifficulty');
        this.usernameInput = document.getElementById('usernameInput');
        this.submitScoreBtn = document.getElementById('submitScore');
        this.playAgainBtn = document.getElementById('playAgain');
        this.backToMenuBtn = document.getElementById('backToMenu');

        // Leaderboard elements
        this.leaderboardList = document.getElementById('leaderboardList');
        this.filterButtons = document.querySelectorAll('.filter-btn');
        this.backFromLeaderboardBtn = document.getElementById('backFromLeaderboard');
    }

    setupEventListeners() {
        // Difficulty selection
        this.difficultyButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                this.selectDifficulty(btn.dataset.difficulty);
            });
        });

        // Menu buttons
        this.startGameBtn.addEventListener('click', () => this.startGame());
        this.showLeaderboardBtn.addEventListener('click', () => this.showLeaderboard());

        // Game over buttons
        this.submitScoreBtn.addEventListener('click', () => this.submitScore());
        this.playAgainBtn.addEventListener('click', () => this.startGame());
        this.backToMenuBtn.addEventListener('click', () => this.showScreen('menuScreen'));

        // Leaderboard buttons
        this.filterButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                this.filterLeaderboard(btn.dataset.difficulty);
            });
        });
        this.backFromLeaderboardBtn.addEventListener('click', () => this.showScreen('menuScreen'));

        // Game controls
        document.addEventListener('keydown', (e) => {
            if (e.code === 'Space') {
                e.preventDefault();
                if (this.game) {
                    this.game.jump();
                }
            }
        });

        // Username input
        this.usernameInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.submitScore();
            }
        });
    }

    selectDifficulty(difficulty) {
        const span = telemetry.startSpan('difficulty_selection', { difficulty });
        
        this.selectedDifficulty = difficulty;
        
        // Update UI
        this.difficultyButtons.forEach(btn => {
            btn.classList.toggle('selected', btn.dataset.difficulty === difficulty);
        });
        
        telemetry.endSpan(span);
    }

    showScreen(screenId) {
        const span = telemetry.startSpan('screen_change', { 
            from: this.currentScreen, 
            to: screenId 
        });
        
        // Hide all screens
        document.querySelectorAll('.screen').forEach(screen => {
            screen.classList.add('hidden');
        });
        
        // Show target screen
        document.getElementById(screenId).classList.remove('hidden');
        this.currentScreen = screenId;
        
        telemetry.endSpan(span);
    }

    async startGame() {
        const span = telemetry.startSpan('start_game', { 
            difficulty: this.selectedDifficulty 
        });
        
        try {
            this.showScreen('gameScreen');
            
            // Initialize game
            this.game = new FlappyKiroGame(this.canvas);
            this.game.setDifficulty(this.selectedDifficulty);
            this.game.onGameOver = (score, difficulty) => this.handleGameOver(score, difficulty);
            
            // Update displays
            this.difficultyDisplay.textContent = `Difficulty: ${this.selectedDifficulty.charAt(0).toUpperCase() + this.selectedDifficulty.slice(1)}`;
            
            // Start game loop for score updates
            this.startScoreUpdates();
            
            // Start the game
            this.game.start();
            
            telemetry.endSpan(span, { success: true });
        } catch (error) {
            telemetry.recordException(span, error);
            telemetry.endSpan(span, { success: false });
            console.error('Failed to start game:', error);
        }
    }

    startScoreUpdates() {
        const updateScore = () => {
            if (this.game && this.game.gameRunning) {
                this.scoreDisplay.textContent = `Score: ${this.game.score}`;
                requestAnimationFrame(updateScore);
            }
        };
        updateScore();
    }

    handleGameOver(score, difficulty) {
        const span = telemetry.startSpan('handle_game_over', { score, difficulty });
        
        this.finalScoreDisplay.textContent = `Score: ${score}`;
        this.finalDifficultyDisplay.textContent = `Difficulty: ${difficulty.charAt(0).toUpperCase() + difficulty.slice(1)}`;
        this.usernameInput.value = '';
        
        this.showScreen('gameOverScreen');
        
        telemetry.endSpan(span);
    }

    async submitScore() {
        const username = this.usernameInput.value.trim();
        const score = this.game ? this.game.score : 0;
        
        if (!username) {
            alert('Please enter a username');
            return;
        }

        const span = telemetry.startSpan('submit_score', {
            username,
            score,
            difficulty: this.selectedDifficulty
        });

        try {
            this.submitScoreBtn.disabled = true;
            this.submitScoreBtn.textContent = 'Submitting...';

            const response = await fetch('/api/leaderboard', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    username,
                    score,
                    difficulty: this.selectedDifficulty
                })
            });

            const data = await response.json();

            if (response.ok) {
                alert('Score submitted successfully!');
                telemetry.endSpan(span, { success: true });
            } else {
                throw new Error(data.error || 'Failed to submit score');
            }
        } catch (error) {
            telemetry.recordException(span, error);
            telemetry.endSpan(span, { success: false });
            alert(`Error: ${error.message}`);
        } finally {
            this.submitScoreBtn.disabled = false;
            this.submitScoreBtn.textContent = 'Submit Score';
        }
    }

    async showLeaderboard(difficulty = 'all') {
        const span = telemetry.startSpan('show_leaderboard', { difficulty });
        
        try {
            this.showScreen('leaderboardScreen');
            await this.loadLeaderboard(difficulty);
            telemetry.endSpan(span, { success: true });
        } catch (error) {
            telemetry.recordException(span, error);
            telemetry.endSpan(span, { success: false });
            console.error('Failed to show leaderboard:', error);
        }
    }

    async loadLeaderboard(difficulty = 'all') {
        const span = telemetry.startSpan('load_leaderboard', { difficulty });
        
        try {
            this.leaderboardList.innerHTML = '<div class="loading">Loading...</div>';
            
            const response = await fetch(`/api/leaderboard?difficulty=${difficulty}`);
            const data = await response.json();

            if (response.ok) {
                this.renderLeaderboard(data);
                telemetry.endSpan(span, { 
                    success: true, 
                    entriesCount: data.length 
                });
            } else {
                throw new Error('Failed to load leaderboard');
            }
        } catch (error) {
            telemetry.recordException(span, error);
            telemetry.endSpan(span, { success: false });
            this.leaderboardList.innerHTML = '<div>Error loading leaderboard</div>';
        }
    }

    renderLeaderboard(entries) {
        if (entries.length === 0) {
            this.leaderboardList.innerHTML = '<div>No scores yet. Be the first!</div>';
            return;
        }

        const html = entries.map((entry, index) => `
            <div class="leaderboard-entry">
                <div class="entry-rank">${index + 1}</div>
                <div class="entry-name">${this.escapeHtml(entry.username)}</div>
                <div class="entry-score">${entry.score}</div>
                <div class="entry-difficulty">${entry.difficulty}</div>
            </div>
        `).join('');

        this.leaderboardList.innerHTML = html;
    }

    filterLeaderboard(difficulty) {
        const span = telemetry.startSpan('filter_leaderboard', { difficulty });
        
        // Update filter buttons
        this.filterButtons.forEach(btn => {
            btn.classList.toggle('active', btn.dataset.difficulty === difficulty);
        });
        
        // Load filtered leaderboard
        this.loadLeaderboard(difficulty);
        
        telemetry.endSpan(span);
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
}

// Initialize app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    const span = telemetry.startSpan('app_initialization');
    try {
        new FlappyKiroApp();
        telemetry.endSpan(span, { success: true });
    } catch (error) {
        telemetry.recordException(span, error);
        telemetry.endSpan(span, { success: false });
        console.error('Failed to initialize app:', error);
    }
});