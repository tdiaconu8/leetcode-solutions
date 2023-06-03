function jsonToMatrix(arr: any[]): any {

    // Get keys
    let keysSet = new Set();
    
    for (const obj of arr) {
        getKeys(obj, "");
    }
    console.log(keysSet)
    const keys = Array.from(keysSet).sort();

    // Build the matrix
    let res = [keys];

    for (const obj of arr) {
        let keyToVal = {};
        let row = [];
        getValues(obj, "", keyToVal);
        for (const key of keys) {
            if (key.toString() in keyToVal) {
                row.push(keyToVal[key.toString()])
            }
            else {
                row.push("");
            }
        }
        res.push(row);
    }

    return res;

    function getValues(obj, path, keyToVal) {
        for (const key in obj) {
            const newPath =  path ? `${path}.${key}` : key;
            if (isObject(obj[key])) {
                getValues(obj[key], newPath, keyToVal);
            }
            else {
                keyToVal[newPath] = obj[key];
            }
        }
    }

    function getKeys(obj, path) {
        for (const key in obj) {
            const newPath = path ? `${path}.${key}` : key;
            if (isObject(obj[key])) {
                getKeys(obj[key], newPath);
            }
            else {
                keysSet.add(newPath);
            }
        }
    }

    function isObject(obj) {
        return typeof obj === "object" && obj !== null;
    }

};