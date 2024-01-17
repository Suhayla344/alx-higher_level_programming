#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - insert num into a sorted list structn
 * @headL pointer to head for linked list
 * @number: number to insert
 * Return: if the func fails - null
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;
	new->next = node->next;
	node->next = new;

	return (new);
}
}
