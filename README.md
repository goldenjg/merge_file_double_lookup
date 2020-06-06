# merge_file_double_lookup
### Python vlookup both directions

This compares 2 files and makes a comprehensive list of both based on the key field
and makes corresponding columns with values from each of the files
it puts missing where it exists in the complete list but not in one of the files
it's similar to what 2 vlookups would look like in Excel, one from list 1 to 2 and one from list 2 to 1


```
File 1
User	Quantity
001234	14
001235	56
001567	23
001582	86

File 2
Users	Quantity  Email
001231	13        j1@gmail.com
001235	56        j2@gmail.com
001568	24        j3@gmail.com
001582	86        j4@gmail.com

Merged File
USERID	quantity1     Quantity2	  Email
1234	    14        missing     missing
1235	    56        56          j2@gmail.com
1567	    23        missing     missing
1582	    86	      86	  j4@gmail.com
1231	    missing   13    j1@gmail.com
1568	    missing   24    j3@gmail.com
```
