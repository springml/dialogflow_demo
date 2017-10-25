package com.sml.demo.banking.model;

/**
 * Created by kaarthikraaj on 23/10/17.
 */



public class User
{
    private String user_id;

    public String getUser_id ()
    {
        return user_id;
    }

    public void setUser_id (String user_id)
    {
        this.user_id = user_id;
    }

    @Override
    public String toString()
    {
        return "ClassPojo [user_id = "+user_id+"]";
    }
}

