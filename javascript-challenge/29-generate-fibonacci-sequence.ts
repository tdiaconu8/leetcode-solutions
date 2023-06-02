function* fibGenerator(): Generator<number, any, number> {

    let a = 0;
    let b = 1;

    while (true) {
        yield a;
        const tmp = a;
        a = b;
        b = tmp + a;
    }

};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */