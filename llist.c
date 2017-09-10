#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include "llist.h"


List *create_new_list() {

    List *list = (List*)malloc(sizeof(List));
    assert(list);
    list->head = list->foot = NULL;
    return list;
}

Item *create_new_item(int val) {

    Item *item = (Item*)malloc(sizeof(Item));
    assert(item);
    item->value = val;
    item->next = NULL;
    return item;
}

void insert_at_head(int val, List *list) {

    Item *item = create_new_item(val);

    /* if head is NULL, so is foot */
    if(list->head == NULL) {
        list->head = list->foot = item; 
    }
    else {
        Item *old_head = list->head;
        item->next = old_head;
        list->head = item;
    }
}

void insert_at_foot(int val, List *list) {

    Item *item = create_new_item(val);

    /* if foot is NULL, so is head */
    if(list->foot == NULL) {
        list->foot = list->head = item;
    }
    else {
        Item *old_foot = list->foot;
        old_foot->next  = item;
        list->foot = item;
    }
}

void print_list(List *list) {

    Item *node = list->head;

    while(node != NULL) {
        printf("%d ",node->value);
        node = node->next;
    }

}

int main(int argc, char *argv[]) {

    List *list = create_new_list();
    insert_at_head(10,list);
    insert_at_foot(100,list);
    insert_at_head(1000,list);
    print_list(list);


    return 0;
}
