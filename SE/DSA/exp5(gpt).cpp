#include <iostream>
#include <cstring>
#include <cctype>
using namespace std;

struct node {
    char data;
    node *left;
    node *right;
};

class stack1 {
    node *data[30];
    int top;
public:
    stack1() {
        top = -1;
    }
    int empty() {
        if (top == -1)
            return 1;
        return 0;
    }
    void push(node *p) {
        data[++top] = p;
    }
    node *pop() {
        return (data[top--]);
    }
};

class tree {
    node *top;
public:
    void expression(char []);
    void display(node *);
    void non_rec_postorder();
    void del(node *);
    node* getTop() const { return top; }
    ~tree();
};

void tree::expression(char prefix[]) {
    char c;
    stack1 s;
    node *t1, *t2;
    int len, i;
    len = strlen(prefix);
    for (i = len - 1; i >= 0; i--) {
        top = new node;
        top->left = NULL;
        top->right = NULL;
        if (isalpha(prefix[i])) {
            top->data = prefix[i];
            s.push(top);
        }
        else if (prefix[i] == '+' || prefix[i] == '*' || prefix[i] == '-' || prefix[i] == '/') {
            t2 = s.pop();
            t1 = s.pop();
            top->data = prefix[i];
            top->left = t2;
            top->right = t1;
            s.push(top);
        }
    }
    top = s.pop();
}

void tree::display(node *root) {
    if (root != NULL) {
        cout << root->data;
        display(root->left);
        display(root->right);
    }
}

void tree::non_rec_postorder() {
    stack1 s;
    node *prev = NULL;
    node *top = this->top; // Accessing top member of the tree
    do {
        while (top != NULL) {
            s.push(top);
            top = top->left;
        }
        while (top == NULL && !s.empty()) {
            top = s.pop();
            if (top->right == NULL || top->right == prev) {
                cout << top->data;
                prev = top;
                top = NULL; // To exit the outer loop
            }
            else {
                s.push(top);
                top = top->right;
            }
        }
    } while (!s.empty());
}

void tree::del(node* root) {
    if (root == NULL)
        return;
    del(root->left);
    del(root->right);
    cout << " Deleting node: " << root->data << endl;
    delete root;
}

tree::~tree() {
    del(top);
}

int main() {
    char expr[20];
    tree t;
    cout << "Enter prefix Expression: ";
    cin >> expr;
    cout << expr;
    t.expression(expr);
    cout << endl;
    cout << "Post-order traversal: ";
    t.non_rec_postorder();
    cout << endl;
    return 0;
}
