package com.example.sharecab;

/**
 * Created by Praveen on 4/2/16.
 */
import android.os.Bundle;
import android.app.Activity;
import java.io.IOException;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
public class ServerCommunication extends Activity {
    private Socket client;
    private PrintWriter printwriter;
    private EditText textField;
    private Button button;
    private String messsage;
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        button.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                messsage = textField.getText().toString(); // get the text message on the text field
                textField.setText(""); // Reset the text field to blank
                try {
                    client = new Socket("127.0.0.1", 8080); // connect to server
                    printwriter = new PrintWriter(client.getOutputStream(),
                            true);
                    printwriter.write(messsage); // write the message to output stream
                    printwriter.flush();
                    printwriter.close();
                    client.close(); // closing the connection
                } catch (UnknownHostException e) {
                    e.printStackTrace();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        });
    }
}