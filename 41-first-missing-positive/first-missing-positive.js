var firstMissingPositive = function(nums) {
    nums.sort((a, b) => a - b);
    let target = 1;
    for (let n of nums) {
        if (n > 0 && n === target) {
            target++;
        } else if (n > target) {
            return target;
        }
    }
    return target;    
};