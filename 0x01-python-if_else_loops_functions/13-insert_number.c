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
	listint_t *new_node, *traverse;
	unsigned int idx = 0, i = 0;
       
	if (head == NULL)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (idx == 0)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	traverse = *head;
	while (i != idx - 1 && traverse != NULL)
	{
		traverse = traverse->next;
		i++;
	}

	if (i == idx - 1 && traverse != NULL)
	{
		new_node->next = traverse->next;
		traverse->next = new_node;
		return (new_node);
	}
	return (NULL);
}
