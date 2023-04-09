// https://leetcode.com/problems/design-an-ordered-stream/
/*
There is a stream of n (idKey, value) pairs arriving in an arbitrary order, where 
 idKey is an integer between 1 and n and value is a string. No two pairs have the same id.

Design a stream that returns the values in increasing order of their IDs by
 returning a chunk (list) of values after each insertion. The concatenation of
  all the chunks should result in a list of the sorted values.

Implement the OrderedStream class:
- OrderedStream(int n) Constructs the stream to take n values.
- String[] insert(int idKey, String value) Inserts the pair (idKey, value) into
    the stream, then returns the largest possible chunk of currently inserted values
    that appear next in the order.

Example:
Input
["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
[[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
Output
[null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]
Explanation
// Note that the values ordered by ID is ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"].
OrderedStream os = new OrderedStream(5);
os.insert(3, "ccccc"); // Inserts (3, "ccccc"), returns [].
os.insert(1, "aaaaa"); // Inserts (1, "aaaaa"), returns ["aaaaa"].
os.insert(2, "bbbbb"); // Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
os.insert(5, "eeeee"); // Inserts (5, "eeeee"), returns [].
os.insert(4, "ddddd"); // Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].
// Concatentating all the chunks returned:
// [] + ["aaaaa"] + ["bbbbb", "ccccc"] + [] + ["ddddd", "eeeee"] = ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"]
// The resulting order is the same as the order above.
 
Constraints:
1 <= n <= 1000
1 <= id <= n
value.length == 5
value consists only of lowercase letters.
Each call to insert will have a unique id.
Exactly n calls will be made to insert.
*/

#include <stdio.h>
#include <malloc.h>

typedef struct{
    int id;
    char *val;
    int left, right;
}node;

node* init_node(int id, char *val){
    node *nw = (node*)malloc(sizeof(node));
    if(nw){
        nw->id = id;
        nw->val = val;
        nw->left = id;
        nw->right = id;
    }
    return nw;
}

typedef struct{
    node **data;
    int next_op;
} OrderedStream;

OrderedStream* orderedStreamCreate(int n) {
    OrderedStream *orderStream = (OrderedStream*)malloc(sizeof(OrderedStream));
    if(orderStream){
        orderStream->data = (node**)calloc(n+2, sizeof(node*));
        orderStream->next_op = 1;
    }
    return orderStream;
}

void join_neighbour(OrderedStream *obj, node *new_node){
    node *left = obj->data[new_node->id-1];
    node *right = obj->data[new_node->id+1];
    int head = -1, tail = -1;
    if(left){
        head = left->right;
        left->right = new_node->id;
        new_node->left = left->id;
    }else{
        head = new_node->id;
    }
    if(right){
        tail = right->left;
        new_node->right = right->id;
        right->left = new_node->id;
    }else{
        tail = new_node->id;
    }
    obj->data[head]->left = tail;
    obj->data[tail]->right = head;
}

char** prepare_result(OrderedStream* obj, int from, int *retSize){
    int count = obj->data[from]->left - obj->data[from]->id + 1;
    *retSize = count;
    char **op = (char**)calloc(count, sizeof(char*));
    if(op){
        int i = 0;
        for(;i<count;i++){
            op[i] = obj->data[i+from]->val;
            obj->data[i+from] = NULL;
        }
        obj->next_op = count+from;
    }
    return op;
}

char ** orderedStreamInsert(OrderedStream* obj, int idKey, char * value, int* retSize) {
    node *new_node = init_node(idKey, value);
    obj->data[idKey] = new_node;
    join_neighbour(obj, new_node);
    if(idKey==obj->next_op){
        char **op = prepare_result(obj, idKey, retSize);
        return op;
    }
    *retSize = 0;
    return NULL;
}

void orderedStreamFree(OrderedStream* obj) {
    free(obj->data);
    free(obj);
}
