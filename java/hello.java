class hello {
	/**
	 * @param args
	 */
	public static void Hello(int i) {

		for(int j=0; j<i; j++) {
			System.out.println("hello " + j);
		}

	}

	public static void main(String[] args) {
		Hello(5);
		System.out.println("DONE");
	}
}