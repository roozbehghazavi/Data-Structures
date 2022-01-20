using System;
using System.Collections.Generic;
using System.Linq;

public class Tree 
{ 
	private void Height(int[] parent, int i, int[] depth) 
	{ 
		if (depth[i] != 0) 
		{ 
			return; 
		} 

		 
		if (parent[i] == -1) 
		{ 
			depth[i] = 1; 
			return; 
		} 

		 
		if (depth[parent[i]] == 0) 
		{ 
			Height(parent, parent[i], depth); 
		} 

		depth[i] = depth[parent[i]] + 1; 
	} 

	private int findHeight(int[] parent, int n) 
	{ 
		int[] depth = new int[n]; 
		
		for (int i = 0; i < n; i++) 
		{ 
			depth[i] = 0; 
		} 


		for (int i = 0; i < n; i++) 
		{ 
			Height(parent, i, depth); 
		} 

		int height2 = depth[0]; 
		for (int i = 1; i < n; i++) 
		{ 
			if (height2 < depth[i]) 
			{ 
				height2 = depth[i]; 
			} 
		} 
		return height2; 
	} 

	public static void Main(string[] args) 
	{ 

		Tree tree = new Tree(); 
		
        string val;
        int n;
   
        val = Console.ReadLine();
        n   = Convert.ToInt32(val);
        
		int[] parent = new int[]{-1, 0, 0, 1, 1, 3, 5}; 
		
		var myString = Console.ReadLine(); 
        int myInt; 
        var array = myString.ToCharArray().Where(x=>  
        int.TryParse(x.ToString(), out myInt)).Select(x=>  
        int.Parse(x.ToString())).ToArray(); 

        Console.WriteLine(tree.findHeight(array, n));
	} 
} 

 
