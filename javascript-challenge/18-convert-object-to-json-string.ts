function jsonStringify(object: any): string {

    // return JSON.stringify(object);
    // We must implent the stringify function there

    // String type
    if (typeof object === "string") return `"${object}"`;

    // number or boolean or null or undefined
    else if (typeof object === "number" 
            || typeof object === "boolean"
            || object === null 
            || object === undefined) 
        return `${object}`;

    // Arrays: we apply recursively jsonStringify to each array element and then we return the array as a string
    if (Array.isArray(object)) {
        object.forEach( function callback(v, i) {
            object[i] = jsonStringify(v);
        });
        return `[${object.join(",")}]`;
    }
    
    // Objects
    else if (typeof object === "object") {
        let objectString = "{";
        const n = Object.keys(object).length;
        for (let i = 0; i < n; i++) {
            let key = Object.keys(object)[i];
            objectString += `${jsonStringify(key)}:${jsonStringify(object[key])}`;
            if (i < n-1) objectString += ",";
        }
        return objectString + "}";
    }

};