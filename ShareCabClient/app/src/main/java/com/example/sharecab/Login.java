package com.example.sharecab;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;

import static java.lang.Thread.sleep;

public class Login extends AppCompatActivity implements View.OnClickListener {
    CheckBox check;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        Button btnClick = (Button) findViewById(R.id.login) ;
        check = (CheckBox) findViewById(R.id.checkBox);
        btnClick.setOnClickListener(this);
    }
    @Override
    public void onClick(View v) {
        if(!check.isChecked()) {
            Intent intent = new Intent(this, pickupmap.class);
            startActivity(intent);
        }
        else
        {
            Intent intent = new Intent(this, driverHome.class);

            startActivity(intent);
        }

    }
    @Override
    public void onBackPressed() {
    }
}
