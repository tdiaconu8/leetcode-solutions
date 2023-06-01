function areDeeplyEqual(o1: any, o2: any): boolean {

    // Check type: if types are different --> false
    if (typeof o1 !== typeof o2) return false;

    // Null or undefined: o1 === o2 ?
    if (o1 === null || o2 === null || o1 === undefined || o2 === undefined) return o1 === o2;

    // If it is not an object, check equality for data types containing values
    if (typeof o1 !== "object") return o1 === o2;

    // Check Array
    if (Array.isArray(o1) || Array.isArray(o2)) {
        if (!Array.isArray(o1) 
            || !Array.isArray(o2)
            || o1.length !== o2.length )
            return false;    // Check if we have two arrays and if they have same length
        for (let i = 0; i < o1.length; i++) {
            if (!areDeeplyEqual(o1[i], o2[i])) return false;
        }
        return true;
    }

    // Check other objects
    else {
        if (Object.keys(o1).length !== Object.keys(o2).length) {
            return false;
        }
        for (const key of Object.keys(o1)) {
            if (!areDeeplyEqual(o1[key], o2[key])) return false;
        }
        return true;
    }

};