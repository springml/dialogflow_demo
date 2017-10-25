package com.sml.demo.banking.model;

/**
 * Created by kaarthikraaj on 23/10/17.
 */



public class Arguments
{
    private String text_value;

    private String name;

    private String raw_text;

    public String getText_value ()
    {
        return text_value;
    }

    public void setText_value (String text_value)
    {
        this.text_value = text_value;
    }

    public String getName ()
    {
        return name;
    }

    public void setName (String name)
    {
        this.name = name;
    }

    public String getRaw_text ()
    {
        return raw_text;
    }

    public void setRaw_text (String raw_text)
    {
        this.raw_text = raw_text;
    }

    @Override
    public String toString()
    {
        return "ClassPojo [text_value = "+text_value+", name = "+name+", raw_text = "+raw_text+"]";
    }
}

