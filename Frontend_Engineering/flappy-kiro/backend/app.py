import json
import os
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
from better_profanity import profanity
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor

# Initialize OpenTelemetry
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

# Configure OTLP exporter
otlp_exporter = OTLPSpanExporter(
    endpoint="http://jaeger:4317",
    insecure=True
)
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

app = Flask(__name__)
CORS(app)

# Instrument Flask app
FlaskInstrumentor().instrument_app(app)

LEADERBOARD_FILE = '/app/data/leaderboard.json'

def load_leaderboard():
    """Load leaderboard from JSON file"""
    with tracer.start_as_current_span("load_leaderboard"):
        if os.path.exists(LEADERBOARD_FILE):
            try:
                with open(LEADERBOARD_FILE, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                tracer.get_current_span().record_exception(e)
                return []
        return []

def save_leaderboard(leaderboard):
    """Save leaderboard to JSON file"""
    with tracer.start_as_current_span("save_leaderboard"):
        try:
            os.makedirs(os.path.dirname(LEADERBOARD_FILE), exist_ok=True)
            with open(LEADERBOARD_FILE, 'w') as f:
                json.dump(leaderboard, f, indent=2)
            return True
        except IOError as e:
            tracer.get_current_span().record_exception(e)
            return False

def validate_username(username):
    """Validate username for appropriateness"""
    with tracer.start_as_current_span("validate_username") as span:
        span.set_attribute("username.length", len(username))
        
        if not username or len(username.strip()) == 0:
            span.set_attribute("validation.result", "empty")
            return False, "Username cannot be empty"
        
        if len(username) > 20:
            span.set_attribute("validation.result", "too_long")
            return False, "Username must be 20 characters or less"
        
        if profanity.contains_profanity(username):
            span.set_attribute("validation.result", "profane")
            return False, "Username contains inappropriate content"
        
        span.set_attribute("validation.result", "valid")
        return True, "Valid username"

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "timestamp": datetime.utcnow().isoformat()})

@app.route('/api/leaderboard', methods=['GET'])
def get_leaderboard():
    """Get top 10 scores from leaderboard"""
    with tracer.start_as_current_span("get_leaderboard") as span:
        difficulty = request.args.get('difficulty', 'all')
        span.set_attribute("difficulty", difficulty)
        
        leaderboard = load_leaderboard()
        
        if difficulty != 'all':
            leaderboard = [entry for entry in leaderboard if entry.get('difficulty') == difficulty]
        
        # Sort by score descending and take top 10
        top_scores = sorted(leaderboard, key=lambda x: x['score'], reverse=True)[:10]
        span.set_attribute("results.count", len(top_scores))
        
        return jsonify(top_scores)

@app.route('/api/leaderboard', methods=['POST'])
def submit_score():
    """Submit a new score to the leaderboard"""
    with tracer.start_as_current_span("submit_score") as span:
        data = request.get_json()
        
        if not data:
            span.set_attribute("error", "no_data")
            return jsonify({"error": "No data provided"}), 400
        
        username = data.get('username', '').strip()
        score = data.get('score')
        difficulty = data.get('difficulty', 'easy')
        
        span.set_attribute("username", username)
        span.set_attribute("score", score)
        span.set_attribute("difficulty", difficulty)
        
        # Validate input
        if score is None or not isinstance(score, int) or score < 0:
            span.set_attribute("error", "invalid_score")
            return jsonify({"error": "Invalid score"}), 400
        
        if difficulty not in ['easy', 'medium', 'hard']:
            span.set_attribute("error", "invalid_difficulty")
            return jsonify({"error": "Invalid difficulty level"}), 400
        
        # Validate username
        is_valid, message = validate_username(username)
        if not is_valid:
            span.set_attribute("error", "invalid_username")
            return jsonify({"error": message}), 400
        
        # Load current leaderboard
        leaderboard = load_leaderboard()
        
        # Add new entry
        new_entry = {
            "username": username,
            "score": score,
            "difficulty": difficulty,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        leaderboard.append(new_entry)
        
        # Save updated leaderboard
        if save_leaderboard(leaderboard):
            span.set_attribute("result", "success")
            return jsonify({"message": "Score submitted successfully", "entry": new_entry}), 201
        else:
            span.set_attribute("error", "save_failed")
            return jsonify({"error": "Failed to save score"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)