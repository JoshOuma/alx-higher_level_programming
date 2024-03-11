function findSecondLargest(...args) {
    const integers = args.map(Number);
    const sortedIntegers = integers.sort((a, b) => b - a);
    if (sortedIntegers.length < 2) {
        console.log(0);
    } else {
        console.log(sortedIntegers[1]);
    }
}
