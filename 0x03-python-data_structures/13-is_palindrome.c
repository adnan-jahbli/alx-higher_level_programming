#include "lists.h"

/**
 * reverse - reverses the second half of the list
 *
 * @second_half: head of the second half
 * Return: no return
 */
void reverse(listint_t **second_half)
{
	listint_t *prev = NULL;
	listint_t *current = *second_half;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*second_half = prev;
}

/**
 * compare - compares each int of the list
 *
 * @first_half: head of the first half
 * @second_half: head of the second half
 * Return: 1 if they are equal, 0 if not
 */
int compare(listint_t *first_half, listint_t *second_half)
{
	listint_t *temp1 = first_half;
	listint_t *temp2 = second_half;

	while (temp1 != NULL && temp2 != NULL)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
		{
			return (0);
		}
	}

	if (temp1 == NULL && temp2 == NULL)
	{
		return (1);
	}

	return (0);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow;
	listint_t *second_half, *middle;
	int is_palindrome;

	slow = fast = prev_slow = *head;
	middle = NULL;
	is_palindrome = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			middle = slow;
			slow = slow->next;
		}

		second_half = slow;
		prev_slow->next = NULL;
		reverse(&second_half);
		is_palindrome = compare(*head, second_half);

		if (middle != NULL)
		{
			prev_slow->next = middle;
			middle->next = second_half;
		}
		else
		{
			prev_slow->next = second_half;
		}
	}

	return (is_palindrome);
}
