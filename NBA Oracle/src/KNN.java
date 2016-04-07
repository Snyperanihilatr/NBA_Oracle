package src;

import java.util.*;
import net.sf.javaml.classification.Classifier;
import net.sf.javaml.classification.KNearestNeighbors;
import net.sf.javaml.core.Dataset;
import net.sf.javaml.core.DefaultDataset;
import net.sf.javaml.core.DenseInstance;
import net.sf.javaml.core.Instance;

public class KNN {
	
	private Dataset data;
	private InfoRow testing;
	private Classifier knn;
	private String[] ranges;
	public KNN(Vector<InfoRow> d, int n, InfoRow test){
		this.ranges = new String[5]; 
		this.knn = new KNearestNeighbors(n);
		this.data = new DefaultDataset();
		this.testing = test;
		classifyWinData(d);
		importData(d);
		this.knn.buildClassifier(this.data);
	}
	
	//Returns Prediction of Classification
	public Object getPrediction(){
		Instance instance = new DenseInstance(this.testing.getRawValues());
		Object prediction = knn.classify(instance);
		
		
		return ranges[(int)(double)prediction];
		
	}
	//Converts raw data into Java-ML Dataset
	private void importData(Vector<InfoRow> dataSet){
		DenseInstance instance;
		for(InfoRow row: dataSet){
			instance = new DenseInstance(row.getRawValues());
			instance.setClassValue( Double.parseDouble(row.getInfoRow().get("won")));
			this.data.add(instance);
		}
	}
	
	//Finds minimum and maximum value in raw data set
	private double[] getMinMax(Vector<InfoRow> dataSet){
		double array[] = new double[2];
		double max = 0.0;
		double min = Double.MAX_VALUE;
		double temp= 0.0;
		for(InfoRow row: dataSet){
			for(String key:row.getInfoRow().keySet()){
				if(key =="won"){
					temp = Double.parseDouble(row.getInfoRow().get(key));
					if(temp> max)
						max = temp;
					if(temp<min)
						min = temp;
				}else
					continue;
			}
		}
		array[0] = min;
		array[1] = max;
		return array;
				
			
	}
	//Finds Specific class for win percentage data
	private int classify(double dataConversion, double minValue, double maxValue) {

		int count = 0;
		int classes = 10;
		double currentValue = minValue;
		double change = (maxValue - minValue)/classes;
		while (currentValue <= dataConversion && currentValue != maxValue) {
			currentValue += change;
			++count;
		}
		return count;
	}
	//Gets ranges of each class
	private void getRanges(double min, double max){
		double change = (max-min)/10;
		double temp = min;
		int upper = 0;
		this.ranges[0] =">="+min+" wins";
		for(int i =1;i<=9;i++){
			
			upper = (int)temp+(int)change;
			this.ranges[i] = Integer.toString((int)(temp+1))+"-"+Integer.toString(upper)+ " wins";
			temp = upper;
		}
		this.ranges[10] = Integer.toString((int)temp+1)+"< wins";

		
	}
	//Classifies Win Data in 10 classes
	private void classifyWinData(Vector<InfoRow> dataSet){

		String newValue;
		double minMax[] = getMinMax(dataSet);
		getRanges(minMax[0],minMax[1]);
		double boatData = 0.0;
		for(InfoRow row:dataSet){
			boatData = Double.parseDouble(row.getInfoRow().get("won"));
			newValue = Double.toString(classify(boatData,minMax[0],minMax[1]));
			row.getInfoRow().put("won", newValue );
			
		}
		
	}

	public Dataset getData() {
		return data;
	}

	public void setData(Dataset data) {
		this.data = data;
	}

	public InfoRow getTesting() {
		return testing;
	}

	public void setTesting(InfoRow testing) {
		this.testing = testing;
	}

	public Classifier getKnn() {
		return knn;
	}

	public void setKnn(Classifier knn) {
		this.knn = knn;
	}

	public String[] getRanges() {
		return ranges;
	}

	public void setRanges(String[] ranges) {
		this.ranges = ranges;
	}
	
	//Remove losses column and divide all other columns by 82
	private void manipulateData(Vector<InfoRow> dataSet){
		double temp = 0.0;
		for(InfoRow row: dataSet){
			for(String key:row.getInfoRow().keySet()){
				if(key == "lost"){
					row.getInfoRow().remove(key);
				}
				else
					temp = Double.parseDouble(row.getInfoRow().get(key));
					temp = temp / 82;
					row.getInfoRow().put(key, String.valueOf(temp));
			}
		}
	}
	
	

}
