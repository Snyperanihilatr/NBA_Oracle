package src;

import java.util.*;
public class InfoRow {
	
	//Create variable for each attribute
	private HashMap<String,String> infoRow;
	//...
	
	public InfoRow(HashMap<String, String> dataSet){
		
		infoRow = new HashMap<String,String>();
		for(String name:dataSet.keySet()){
			infoRow.put(name.toLowerCase(), dataSet.get(name));
		}
		
		
		
		
	}
	
	//Returns Raw double values for Java-ML Instance. Excludes boatCount
	public double[] getRawValues(){
		double [] values = new double[this.infoRow.size()-1];
		int count = 0;
		for(String name:new TreeSet<String>(this.infoRow.keySet())){
			if (name=="boatcount")
				continue;
			values[count] = Double.parseDouble(this.infoRow.get(name));
			count++;
		}
		return values;
	}
	public HashMap<String,String>getInfoRow(){
		return this.infoRow;
	}




	
	
	
		

}