import java.io.*;
import java.nio.file.*;
import java.util.*;

public class Main {

    private final static Path FILE_PATH = Paths.get("user_tasks.txt");
    private static List<String> tasks = new ArrayList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean isUsing = true;
        loadTasks();

        while (isUsing) {
            showMenu();
            System.out.print(">>> ");
            try {
                String userInput = scanner.nextLine();

                switch (userInput) {
                    case "1" -> showAllTasks();
                    case "2" -> {
                        System.out.print("Task: ");
                        String task = scanner.nextLine();
                        addTask(task);
                    }
                    case "3" -> {
                        System.out.print("Task number: ");
                        int task = scanner.nextInt() - 1;
                        scanner.nextLine();
                        removeTask(task);
                    }
                    case "4" -> {
                        System.out.print("Are you sure you want to clear list? (y/n): ");
                        String userChoice = scanner.nextLine().toLowerCase();
                        if (userChoice.equals("y")) {
                            clearList();
                            System.out.println("Successfully cleared.");
                        }
                    }
                    case "5" -> isUsing = false;
                    default -> System.out.println("Invalid Input.");
                }
            } catch (InputMismatchException e) {
                System.out.println("An error occurred.");
            }
        }
    }

    private static void showAllTasks() {
        if (tasks.isEmpty()) {
            System.out.println("List is empty.");
            return;
        }

        for (int i = 0; i < tasks.size(); i++) {
            System.out.println((i + 1) + ". " + tasks.get(i));
        }
    }

    private static void addTask(String task) {
        tasks.add(task);
        saveTask();
    }

    private static void removeTask(int taskIndex) {
        if (taskIndex < 0 || taskIndex >= tasks.size()) {
            System.out.println("Invalid index.");
            return;
        }

        tasks.remove(taskIndex);
        saveTask();
    }

    private static void clearList() {
        tasks.clear();
        saveTask();
    }

    private static void saveTask() {
        try (BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(FILE_PATH.toFile()))) {
            for (String task : tasks) {
                bufferedWriter.write(task);
                bufferedWriter.newLine();
            }
        } catch (IOException e) {
            System.out.println("An error occurred.");
        }
    }

    private static void loadTasks() {
        try {
            if (!Files.exists(FILE_PATH)) {
                Files.createFile(FILE_PATH);
            }
        } catch (IOException e) {
            System.out.println("An error occurred.");
        }

        try (BufferedReader bufferedReader = new BufferedReader(new FileReader(FILE_PATH.toFile()))) {

            String line;
            while ((line = bufferedReader.readLine()) != null) {
                tasks.add(line);
            }
        } catch (IOException e) {
            System.out.println("An error occurred.");
        }
    }

    private static void showMenu() {
        System.out.println("""
                ===============
                1. Show List
                2. Add Task
                3. Remove Task
                4. Clear List
                5. Quit
                ===============
                """);
    }
}