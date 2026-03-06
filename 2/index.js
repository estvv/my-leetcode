/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let res = new ListNode(0);
    let current = res;
    let carry = 0;

    while (l1 || l2 || carry != 0) {
        let l1_value = 0;
        let l2_value = 0;

        if (l1) {
            l1_value = l1.val;
        }
        if (l2) {
            l2_value = l2.val;
        }

        let sum = l1_value + l2_value + carry;
        let value = sum % 10;

        carry = Math.floor(sum / 10);

        current.next = new ListNode(value);
        current = current.next;

        if (l1) {
            l1 = l1.next
        }
        if (l2) {
            l2 = l2.next;
        }
    }
    return res.next;
};
