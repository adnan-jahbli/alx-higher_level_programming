#include "lists.h"

/**
 * check_cycle - a function that checks if a singly linked list has
 * a cycle in it
 * @list: a pointer to the singly linked list
 * Return: 0 if there is no cycle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr;
	listint_t *prv;

	ptr = list;
	prv = list;
	while (list && ptr && ptr->next)
	{
		list = list->next;
		ptr = ptr->next->next;

		if (list == ptr)
		{
			list = prv;
			prv =  ptr;
			while (1)
			{
				ptr = prv;
				while (ptr->next != list && ptr->next != prv)
					ptr = ptr->next;
				if (ptr->next == list)
					break;
				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
