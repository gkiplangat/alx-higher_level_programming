#include "lists.h"
#include "/usr/include/python3.4/Python.h"
#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/object.h"

/**
 * print_piython_list_info - prints information related to Python lists
 * @p: Pointer to the Python object.
 *
 * Return: Nothing.
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	Py_ssize_t e;
	PyObject *itemObj;
	const char *itemType;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (e = 0; e < size; e++)
	{
		itemObj = PyList_GetItem(p, e);
		itemType = Py_TYPE(itemObj)->tp_name;
		printf("Element %ld: %s\n", e, itemType);
	}
}
