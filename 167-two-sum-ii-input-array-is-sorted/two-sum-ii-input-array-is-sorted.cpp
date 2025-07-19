class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int a = 0;
        int b = numbers.size() - 1;

        vector<int> res;
        while (a < b) {
            int sum = numbers[a] + numbers[b]; 
            if (sum < target) {
                a++;
            } else if (sum > target) {
                b--;
            } else {
                res.push_back(a + 1);
                res.push_back(b + 1);
                break;
            }
        }
        return res;
    }
};
