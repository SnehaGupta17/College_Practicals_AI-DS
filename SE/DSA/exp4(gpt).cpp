#include <iostream>
#include <queue>

using namespace std;

struct node {
    int data;
    node *left, *right;
};

class tree {
public:
    node *root;

    tree() { root = NULL; }

    void create();
    void insert(node *&, int);
    int longest_path(node *);
    void mirror(node *);
    void level_wise(node *);
    void min(node *);
    void search(node *, int);
};

void tree::create() {
    char ch;
    do {
        int data;
        cout << "Enter data: ";
        cin >> data;
        insert(root, data);
        cout << "Do you want to continue? (y/n): ";
        cin >> ch;
    } while (ch == 'y');
}

void tree::insert(node *&root, int data) {
    if (root == NULL) {
        root = new node;
        root->data = data;
        root->left = root->right = NULL;
    } else if (data < root->data)
        insert(root->left, data);
    else
        insert(root->right, data);
}

int tree::longest_path(node *root) {
    if (root == NULL)
        return 0;
    return max(longest_path(root->left), longest_path(root->right)) + 1;
}

void tree::mirror(node *root) {
    if (root == NULL)
        return;
    else {
        node *temp = root->left;
        root->left = root->right;
        root->right = temp;
        mirror(root->left);
        mirror(root->right);
    }
}

void tree::level_wise(node *root) {
    if (root == NULL)
        return;
    queue<node *> q;
    q.push(root);
    while (!q.empty()) {
        node *current = q.front();
        cout << current->data << " ";
        q.pop();
        if (current->left != NULL)
            q.push(current->left);
        if (current->right != NULL)
            q.push(current->right);
    }
}

void tree::min(node *root) {
    if (root == NULL)
        return;
    while (root->left != NULL)
        root = root->left;
    cout << "Minimum value: " << root->data << endl;
}

void tree::search(node *root, int x) {
    if (root == NULL) {
        cout << "Not found" << endl;
        return;
    }
    if (root->data == x) {
        cout << "Found" << endl;
        return;
    }
    if (x < root->data)
        search(root->left, x);
    else
        search(root->right, x);
}

int main() {
    tree t1;
    int op, x;
    do {
        cout << "\n1) Insert Node\n2) Mirror Image\n3) Longest Path\n4) Level Wise Traversal\n5) Minimum Value\n6) Search\n7) Exit\nEnter Your Choice: ";
        cin >> op;
        switch (op) {
            case 1:
                t1.create();
                break;
            case 2:
                t1.mirror(t1.root);
                cout << "Mirror Image created" << endl;
                break;
            case 3:
                cout << "Longest Path Length: " << t1.longest_path(t1.root) << endl;
                break;
            case 4:
                cout << "Level Wise Traversal: ";
                t1.level_wise(t1.root);
                cout << endl;
                break;
            case 5:
                t1.min(t1.root);
                break;
            case 6:
                cout << "Enter value to search: ";
                cin >> x;
                t1.search(t1.root, x);
                break;
            case 7:
                cout << "Exiting program" << endl;
                break;
            default:
                cout << "Invalid choice" << endl;
        }
    } while (op != 7);
    return 0;
}
