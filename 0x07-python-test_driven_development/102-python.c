#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - a function that prints Python strings.
 *
 * @p: Python Object
 */
void print_python_string(PyObject *p)
{
	PyUnicodeObject *pyUnicode = (PyUnicodeObject *) p;

	if (!PyUnicode_Check(pyUnicode))
	{
		fprintf(stderr, "TypeError: print_python_string() argument must be a string\n");
		return;
	}
	printf("  %.*s", (int) PyUnicode_GET_LENGTH(pyUnicode), PyUnicode_AsUTF8(pyUnicode));
	printf("\n");
}
