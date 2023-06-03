function objDiff(obj1: any, obj2: any): any {

    function isObject(obj) {
        return typeof obj === "object" && obj !== null;
    }

    if (!isObject(obj1) && !isObject(obj2)) {   // Both primitives
        return obj1 !== obj2 ? [obj1, obj2] : [];
    };

    if (isObject(obj1) !== isObject(obj2)) {    // One primitive
        return [obj1, obj2]
    }

    if (Array.isArray(obj1) !== Array.isArray(obj2)) { // One array, one object
        return [obj1, obj2];
    }

    let res = {};

    for (const key in obj1) {
        if (key in obj2) {
            let diff = objDiff(obj1[key], obj2[key]);
            if (Object.keys(diff).length > 0) {
                res[key] = diff;
            }
        }
    }

    return res;

};