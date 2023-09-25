#include <stdio.h>
#include <Python.h>
/**
 * print_python_list - prints some basic info about Python lists
 * @p: pointer to PyObject list
 */
void print_python_list(PyObject *p)
{
	PyObject *obj;
	long int size, k;
	PyListObject *list;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		setbuf(stdout, NULL);
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (k = 0; k < size; k++)
	{
		obj = list->ob_item[k];

		printf("Element %ld: %s\n", k, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
		if (PyFloat_Check(obj))
			print_python_float(obj);
			
	}
	setbuf(stdout, NULL);
}
/**
 * print_python_bytes - prints some basic info about Python bytes
 * @p: pointer to PyObject bytes
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, k, limit;

	setbuf(stdout, NULL);

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		setbuf(stdout, NULL);
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (k = 0; k < limit; k++)
		if (string[k] >= 0)
			printf(" %02x", string[k]);
		else
			printf(" %02x", 256 + string[k]);

	printf("\n");
	setbuf(stdout, NULL);
}
/**
 * print_python_float - prints some basic info about Python float objects
 * @p: pointer to PyObject float
 */
void print_python_float(PyObject *p)
{
	double value;
	char *no_f;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		setbuf(stdout, NULL);
		return;
	}

	value = ((PyFloatObject *)(p))->ob_fval;
	no_f = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);

	printf("  value: %s\n", no_f);
	setbuf(stdout, NULL);
}
