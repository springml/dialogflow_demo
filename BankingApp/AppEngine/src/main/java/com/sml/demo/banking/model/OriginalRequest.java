package com.sml.demo.banking.model;

/**
 * Created by kaarthikraaj on 23/10/17.
 */



public class OriginalRequest
{
    private String source;

    private Data data;

    public String getSource ()
    {
        return source;
    }

    public void setSource (String source)
    {
        this.source = source;
    }

    public Data getData ()
    {
        return data;
    }

    public void setData (Data data)
    {
        this.data = data;
    }

    @Override
    public String toString()
    {
        return "ClassPojo [source = "+source+", data = "+data+"]";
    }
}


