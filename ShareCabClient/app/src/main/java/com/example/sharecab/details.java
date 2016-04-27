package com.example.sharecab;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.*;
public class details extends AppCompatActivity  implements View.OnClickListener {
    private String[] arraySpinner;
    LinearLayout layoutOfPopup;
    PopupWindow popupMessage;
    Button but1;
    Button popupButton, insidePopupButton;
    TextView popupText;
    CheckBox check,check2;
    EditText t1,t2;
    Spinner s2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_details);
        this.arraySpinner = new String[]{
                "1", "2", "3", "4"
        };
        t1 = (EditText) findViewById(R.id.editText4);
        t2 = (EditText) findViewById(R.id.editText2);
        s2 = (Spinner) findViewById(R.id.spinner2);
        s2.setVisibility(View.INVISIBLE);
        Spinner s = (Spinner) findViewById(R.id.spinner);
        Spinner s1 = (Spinner) findViewById(R.id.spinner2);
        check = (CheckBox) findViewById(R.id.checkBox3);
        check2 = (CheckBox) findViewById(R.id.checkBox2);
        ArrayAdapter<String> adapter = new ArrayAdapter<String>(this,
                android.R.layout.simple_spinner_item, arraySpinner);
        s.setAdapter(adapter);
        s1.setAdapter(adapter);
         but1 = (Button) findViewById(R.id.button2);
        but1.setOnClickListener(this);
        check.setOnClickListener(this);
        check2.setOnClickListener(this);
    }

    @Override
    public void onClick(View view) {
        switch (view.getId()) {
            case R.id.button2:
                Intent intent = new Intent(this, home.class);
                startActivity(intent);
                break;
            case R.id.checkBox3:
                if(check.isChecked()) {
                    t1.setVisibility(View.INVISIBLE);
                    t2.setVisibility(View.INVISIBLE);
                }
                else
                {
                    t1.setVisibility(View.VISIBLE);
                    t2.setVisibility(View.VISIBLE);
                }
                break;
            case R.id.checkBox2:
                if(!check2.isChecked()) {
                    s2.setVisibility(View.INVISIBLE);
                }
                else
                {
                    s2.setVisibility(View.VISIBLE);
                }
                break;
        }

    }
}