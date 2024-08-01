# leetcode id-deepali0402
class StockSpanner {
public:
    StockSpanner() {
        
    }
    
    int next(int price) {
        int sp=1;
        while(!st.empty() && st.top().first<=price){
            sp+=st.top().second;
            st.pop();
        }
        st.push({price,sp}) ;
        return sp;
        
    }

private:
    stack <pair<int,int>> st;
};

