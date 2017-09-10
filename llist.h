typedef int Value;

typedef struct Item {
    Value value;
    struct Item *next;
} Item;

typedef struct List {
    Item *head;
    Item *foot;
} List;


List *create_new_list();
Item *create_new_item(int val);
void insert_at_head(int val, List *list);
void insert_at_foot(int val, List *list);
void print_list(List *list);


