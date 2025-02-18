/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *result = new ListNode();
        result -> next = NULL;
        int extra = 0;
        ListNode *current = new ListNode();
        current ->next = NULL;
        result = current;
        int v1, v2;
        while(l1 != NULL || l2 != NULL){
            int add_num;
            if(l1 == NULL){
                v1 = 0;
                v2 = l2->val;
            }
            else if(l2 == NULL){
                v2 = 0;
                v1 = l1->val;
            }
            else{
                v1 = l1->val;
                v2 = l2->val;
            }
            add_num = v1 + v2;
            if(extra == 1){
                add_num += 1;
            }
            if(add_num > 9){
                extra = 1;
                add_num = add_num - 10;
            }
            else extra = 0;
            current->val = add_num;
            
            //current -> next = NULL;
            if(l1 == NULL){
                l2 = l2->next;
            }
            else if(l2 == NULL){
                l1 = l1->next;
            }
            else{
                l1 = l1->next;
                l2 = l2->next;
            }
            if(l1 != NULL || l2 != NULL){
                current->next = new ListNode();
                current = current -> next;
            }
        }
        if(extra == 1){
            current->next = new ListNode();
            current = current -> next;
            current->val = 1;
            current->next = NULL;
        }
        else {
            
            current = nullptr;
        }
        return result;
    }
};