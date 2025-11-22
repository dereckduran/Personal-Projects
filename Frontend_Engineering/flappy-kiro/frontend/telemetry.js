// Simple telemetry implementation for frontend logging
class Telemetry {
    constructor() {
        this.serviceName = 'flappy-kiro-frontend';
        this.traces = [];
    }

    startSpan(name, attributes = {}) {
        const span = {
            name,
            startTime: Date.now(),
            attributes: {
                service: this.serviceName,
                ...attributes
            },
            events: []
        };
        
        console.log(`[OTEL] Starting span: ${name}`, attributes);
        return span;
    }

    endSpan(span, attributes = {}) {
        span.endTime = Date.now();
        span.duration = span.endTime - span.startTime;
        span.attributes = { ...span.attributes, ...attributes };
        
        this.traces.push(span);
        console.log(`[OTEL] Ending span: ${span.name} (${span.duration}ms)`, span.attributes);
        
        // Send to backend for logging (in a real implementation)
        this.sendTrace(span);
    }

    addEvent(span, name, attributes = {}) {
        const event = {
            name,
            timestamp: Date.now(),
            attributes
        };
        span.events.push(event);
        console.log(`[OTEL] Event: ${name}`, attributes);
    }

    recordException(span, error) {
        this.addEvent(span, 'exception', {
            'exception.type': error.constructor.name,
            'exception.message': error.message,
            'exception.stacktrace': error.stack
        });
    }

    async sendTrace(span) {
        try {
            // In a real implementation, this would send to an OTEL collector
            // For now, we'll just log it
            console.log('[OTEL] Trace data:', {
                traceId: this.generateTraceId(),
                spanId: this.generateSpanId(),
                ...span
            });
        } catch (error) {
            console.error('[OTEL] Failed to send trace:', error);
        }
    }

    generateTraceId() {
        return Math.random().toString(16).substr(2, 16);
    }

    generateSpanId() {
        return Math.random().toString(16).substr(2, 8);
    }

    // Convenience method for timing operations
    async timeOperation(name, operation, attributes = {}) {
        const span = this.startSpan(name, attributes);
        try {
            const result = await operation();
            this.endSpan(span, { success: true });
            return result;
        } catch (error) {
            this.recordException(span, error);
            this.endSpan(span, { success: false, error: error.message });
            throw error;
        }
    }
}

// Global telemetry instance
window.telemetry = new Telemetry();