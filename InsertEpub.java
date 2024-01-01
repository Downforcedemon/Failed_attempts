package sci_fi_app;

import java.io.File;
import java.io.FileInputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

public class InsertEpub {
    public static void main(String[] args) {
        String url = "jdbc:postgresql://192.168.0.48/Sci-fi"; // 
        String user = "postgres";              
        String password = "password"; 

        try {
            Connection conn = DriverManager.getConnection(url, user, password);
            File file = new File("/home/kali/Downloads/Culture_Series/Inversions.epub");
            FileInputStream fis = new FileInputStream(file);

            PreparedStatement ps = conn.prepareStatement("UPDATE books SET bookcontent = ? WHERE bookid = ?");
            ps.setBinaryStream(1, fis, (int) file.length());
            ps.setString(2, "1");
            ps.executeUpdate();

            // Clean up
            ps.close();
            fis.close();
            conn.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
