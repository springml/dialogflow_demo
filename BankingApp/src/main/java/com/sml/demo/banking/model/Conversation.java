package com.sml.demo.banking.model;

/**
 * Created by kaarthikraaj on 23/10/17.
 */


public class Conversation
{
    private String conversation_id;

    private String conversation_token;

    private String type;

    public String getConversation_id ()
    {
        return conversation_id;
    }

    public void setConversation_id (String conversation_id)
    {
        this.conversation_id = conversation_id;
    }

    public String getConversation_token ()
    {
        return conversation_token;
    }

    public void setConversation_token (String conversation_token)
    {
        this.conversation_token = conversation_token;
    }

    public String getType ()
    {
        return type;
    }

    public void setType (String type)
    {
        this.type = type;
    }

    @Override
    public String toString()
    {
        return "ClassPojo [conversation_id = "+conversation_id+", conversation_token = "+conversation_token+", type = "+type+"]";
    }
}

