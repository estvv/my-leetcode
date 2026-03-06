/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

// function ListNode(val, next) {
//     this.val = (val===undefined ? 0 : val)
//     this.next = (next===undefined ? null : next)
// }

/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    let sorted = new ListNode(0);
    let head = sorted;

    while (list1 || list2) {
        if (!list1) {
            head.next = new ListNode(0);
            head.next.val = list2.val;
            head = head.next;
            list2 = list2.next
        } else if (!list2) {
            head.next = new ListNode(0);
            head.next.val = list1.val;
            head = head.next;
            list1 = list1.next
        } else {
            head.next = new ListNode(0);
            if (list1.val <= list2.val) {
                head.next.val = list1.val;
                list1 = list1.next
            } else {
                head.next.val = list2.val;
                list2 = list2.next
            }
            head = head.next;
        }
    }
    return sorted.next;
};
