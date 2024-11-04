package Project;

import java.sql.Connection;
import java.sql.DriverManager;

public class ConnectionProvider {
    
    /**
     * Establishes a connection to the database.
     * @return Connection object if successful, otherwise null.
     */
    public static Connection getCon() {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver"); // Updated for newer MySQL versions
            return DriverManager.getConnection("jdbc:mysql://localhost:3306/censusmanagement", "root", "");
        } catch (Exception e) {
            System.out.println("Connection failed: " + e.getMessage()); // Logs any error message for debugging
            return null;
        }
    }
    
    // Removed unsupported getcon method for clarity as per submission requirement
}
