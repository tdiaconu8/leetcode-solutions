class TimeLimitedCache {

    cache = new Map();

    constructor() {
    }

    set(key: number, value: number, duration: number): boolean {
        const alreadyExists = this.cache.get(key);
        if (alreadyExists) {
            clearTimeout(alreadyExists.timeoutID);
        }
        const timeoutID = setTimeout( () => {
            this.cache.delete(key)
        },
        duration);
        this.cache.set(key, {value, timeoutID});
        return Boolean(alreadyExists)
    }

    get(key: number): number {
        if (this.cache.get(key)) {
            return this.cache.get(key).value;
        }
        else {
            return -1;
        }
    }

	count(): number {
        return this.cache.size;
    }
}

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */