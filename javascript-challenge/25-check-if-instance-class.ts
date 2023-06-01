function checkIfInstanceOf(obj: any, classFunction: any): boolean {

    if (obj === null || obj === undefined || classFunction === undefined || classFunction === null) {
        return false;
    }
    let proto = Object.getPrototypeOf(obj);

    while (proto !== null) {
        if (proto === classFunction.prototype) {
            return true;
        }
        proto = Object.getPrototypeOf(proto);
    }
    return false;

};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */