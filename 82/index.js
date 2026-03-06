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
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function(head) {
    for (let tmp = head; tmp != null; tmp = tmp.next) {
        if (tmp.next == null) {
            break;
        }

        while (tmp.next != null && tmp.next.val == tmp.val) {
            tmp.next = tmp.next.next;
        }
    }
    return head;
};

console.log(deleteDuplicates(new ListNode(1, new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(3)))))));
