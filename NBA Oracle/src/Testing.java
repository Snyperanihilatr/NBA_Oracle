import java.io.File;
import java.io.IOException;
import java.util.*;

import net.sf.javaml.classification.Classifier;
import net.sf.javaml.classification.KNearestNeighbors;
import net.sf.javaml.core.Dataset;
import net.sf.javaml.core.Instance;
import net.sf.javaml.tools.data.FileHandler;
public class Testing {
	
	
	public static void main(String[] args) throws IOException {

		Dataset data = FileHandler.loadDataset(new File("Testing.csv"), 12, ",");
		Dataset dataForClassification = FileHandler.loadDataset(new File("Testing.csv"), 12, ",");
		 /* Contruct a KNN classifier that uses 5 neighbors to make a
		  *decision. */
		double correct = 0, wrong = 0;
		Classifier knn;
		double result = 0.0;
		double rate = 0.0;
		int k = 0;
		Vector<Double> kValues = new Vector<Double>();
		for(int i = 1;i<=50;i++){
			
		
			knn = new KNearestNeighbors(i);
			knn.buildClassifier(data);
			
			
			/* Counters for correct and wrong predictions. */
			
			/* Classify all instances and check with the correct class values */
			for (Instance inst : dataForClassification) {
			    Object predictedClassValue = knn.classify(inst);
			    Object realClassValue = inst.classValue();
			    if (predictedClassValue.equals(realClassValue))
			        correct++;
			    else
			        wrong++;
			}
			rate = correct/(correct+wrong);
			if(rate>result){
				result = rate;
				k = i;
			}
			kValues.add(rate);
			System.out.println(i+": "+rate);
			correct = 0.0;
			wrong = 0.0;
		}
		System.out.print(k+": "+result);
	}

}
