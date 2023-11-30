#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node - function that inserts a number to a singly linked list.
 * @head: pointer to pointer to head of the list.
 * @number: value of the node to insert.
 *
 * Return: the address of the new node, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	listint_t *new = malloc(sizeof(listint_t));
       
	if (!new)
		return (NULL);
	new->n  = number;
	new->next = NULL;

	if (!node || new->n < node->n)
	{
		new->next = node;
		return (*head = new);
	}

	while (node)
	{
		if  (!node->next || new->n < node->next->n)
		{
			new->next = node->next;
			node->next = new;
			return (node);
		}
		node = node->next;
	}
	free(new);
	return (NULL);
}
