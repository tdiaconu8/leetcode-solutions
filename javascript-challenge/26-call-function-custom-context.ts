declare global { 
    interface Function {
      callPolyfill(context: Record<any, any>, ...args: any[]): any;
	}
}

Function.prototype.callPolyfill = function(context, ...args): any {

    const bind = this.bind(context);    // Bind the function with the context
    return bind.apply(context, args);   // Then we apply all params
}

/**
 * function increment() { this.count++; return this.count; }
 * increment.callPolyfill({count: 1}); // 2
 */
 /**
 * @param {Object} context
 * @param {any[]} args
 * @return {any}
 */