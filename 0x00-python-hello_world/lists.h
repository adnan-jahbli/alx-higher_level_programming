#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - a singly linked list
 * @n: an integer variable
 * @next: a pointer to the next node
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

#endif
