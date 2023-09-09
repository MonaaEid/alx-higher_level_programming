#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current, *reverse, *temp;
	int result;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);
	current = *head;
	reverse = NULL;
	while (current != NULL)
	{
		temp = malloc(sizeof(listint_t));
		if (temp == NULL)
			return (0);
		temp->n = current->n;
		temp->next = reverse;
		reverse = temp;
		current = current->next;
	}
	result = 1;
	current = *head;
	while (current != NULL && reverse != NULL)
	{
		if (current->n != reverse->n)
		{	result = 0;
			break;
		}
		current = current->next;
		reverse = reverse->next;
	}
	while (reverse != NULL)
	{
		temp = reverse;
		reverse = reverse->next;
		free(temp);
	}
	return (result);
}
