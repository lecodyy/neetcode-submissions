class MinStack {
public:
    std::stack<int> stack;
    std::stack<int> min_stack;


    MinStack() {
        
    }
    
    void push(int val) {
        stack.push(val);
        if (min_stack.empty()) {
            min_stack.push(val);
        } 
        else {
            min_stack.push(std::min(val, min_stack.top()));
        }

    }
    
    void pop() {
        stack.pop();
        min_stack.pop();

    }
    
    int top() {
        return stack.top();
    }
    
    int getMin() {
        return min_stack.top();
        
    }
};
