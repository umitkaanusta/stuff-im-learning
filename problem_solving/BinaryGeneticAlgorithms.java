package problem_solving;

import java.util.function.ToDoubleFunction;
import java.util.Collections;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.lang.StringBuilder;

public class BinaryGeneticAlgorithms {
	Random rg = new Random();
	
	private String generate(int length) {
		StringBuilder strb = new StringBuilder(length);
		for(int i = 0; i < length; i++) {
			int newInt = rg.nextBoolean() ? 1 : 0;
			strb.append(newInt);
		}
		return strb.toString();
	}
	    
	private String[] select(List<String> population, List<Double> fitnesses) {
		// select 2 most fittest
		Map<String, Double> map = new HashMap<String, Double>();
		for(int i = 0; i < population.size(); i++) {
			map.put(population.get(i), fitnesses.get(i));
		}
		String maxKey = Collections.max(map.entrySet(), Map.Entry.comparingByValue()).getKey();
		map.remove(maxKey);
		String secondMaxKey = Collections.max(map.entrySet(), Map.Entry.comparingByValue()).getKey();
		String[] selected = {maxKey, secondMaxKey};
		return selected;
	}
	  
	private String mutate(String chromosome, double p) {
	    // p = likelihood of mutation for each bit
		StringBuilder strb = new StringBuilder(chromosome);
		for(int i = 0; i < chromosome.length(); i++) {
			if(rg.nextDouble() <= p) {
				char curr = strb.charAt(i);
				if(curr == '0') {
					strb.setCharAt(i, '1');
				}
				else {
					strb.setCharAt(i, '0');
				}
			}
		}
	    return strb.toString();
	}
	  
	private String[] crossover(String chromosome1, String chromosome2) {
	    int cutOffIndex = rg.nextInt(chromosome1.length());
	    StringBuilder strb1 = new StringBuilder(chromosome1);
	    StringBuilder strb2 = new StringBuilder(chromosome2);
	    for(int i = cutOffIndex; i < chromosome1.length(); i++) {
	    	char temp = strb2.charAt(i);
	    	strb2.setCharAt(i, strb1.charAt(i));
	    	strb1.setCharAt(i, temp);
	    }
	    String[] chromosomes = {strb1.toString(), strb2.toString()};
	    return chromosomes;
	}
	  
	public String run(ToDoubleFunction<String> fitness, int length, double p_c, double p_m) {
		return run(fitness, length, p_c, p_m, 100);
	}
	  
	public String run(ToDoubleFunction<String> fitness, int length, double p_c, double p_m, int iterations) {
		int popSize = 200;
		List<String> population = new ArrayList<String>();
		for(int i = 0; i < popSize; i++) {
			population.add(this.generate(length));
		}
		double maxFitness = 0;
		List<String> nextPopulation;
		List<Double> fitnesses = new ArrayList<Double>();
		
		while(iterations != 0) {
			fitnesses = new ArrayList<Double>();
			for(String s: population) {
				fitnesses.add(fitness.applyAsDouble(s));
			}
			maxFitness = Collections.max(fitnesses);
			if(maxFitness == 1) break;
			
			nextPopulation = new ArrayList<String>();
			while(nextPopulation.size() < population.size()) {
				String[] selected = this.select(population, fitnesses);
				String[] offsprings = (Math.random() < p_c) ? this.crossover(selected[0], selected[1]) : selected;
				nextPopulation.add(this.mutate(offsprings[0], p_m));
				nextPopulation.add(this.mutate(offsprings[1], p_m));
			}
			population = nextPopulation;
			iterations--;
		}
		return population.get(fitnesses.indexOf(maxFitness));
	}

}
