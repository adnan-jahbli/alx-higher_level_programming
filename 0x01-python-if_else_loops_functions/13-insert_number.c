#include "lists.h"

/**
 * insert_node - a function that inserts a new node at a given position.
 * @head: head of the list.
 * @number: index to where the new node is added.
 *
 * Return: the address of the new node or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *temp, *prev_node;

	temp = *head;
	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		return (NULL);
	}

	while (temp != NULL)
	{
		if (temp->n > number)
			break;
		prev_node = temp;
		temp = temp->next;
	}

	new_node->n = number;

	if (*head == NULL)
	{
		new_node->next = NULL;
		*head = new_node;
	}
	else
	{
		new_node->next = temp;
		if (temp == *head)
			*head = new_node;
		else
			prev_node->next = new_node;
	}

	return (new_node);
}
